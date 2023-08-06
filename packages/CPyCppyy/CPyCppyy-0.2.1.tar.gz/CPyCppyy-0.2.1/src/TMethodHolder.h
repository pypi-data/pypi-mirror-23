#ifndef CPYCPPYY_TMETHODHOLDER_H
#define CPYCPPYY_TMETHODHOLDER_H

// Bindings
#include "PyCallable.h"

// Standard
#include <string>
#include <vector>


namespace CPyCppyy {

   class TExecutor;
   class TConverter;

   class TMethodHolder : public PyCallable {
   public:
      TMethodHolder( Cppyy::TCppScope_t scope, Cppyy::TCppMethod_t method );
      TMethodHolder( const TMethodHolder& );
      TMethodHolder& operator=( const TMethodHolder& );
      virtual ~TMethodHolder();

   public:
      virtual PyObject* GetSignature( Bool_t show_formalargs = kTRUE );
      virtual PyObject* GetPrototype( Bool_t show_formalargs = kTRUE );
      virtual Int_t GetPriority();

      virtual Int_t GetMaxArgs();
      virtual PyObject* GetCoVarNames();
      virtual PyObject* GetArgDefault( Int_t iarg );
      virtual PyObject* GetScopeProxy();

      virtual PyCallable* Clone() { return new TMethodHolder( *this ); }

   public:
      virtual PyObject* Call(
         ObjectProxy*& self, PyObject* args, PyObject* kwds, TCallContext* ctxt = 0 );

      virtual Bool_t Initialize( TCallContext* ctxt = 0 );
      virtual PyObject* PreProcessArgs( ObjectProxy*& self, PyObject* args, PyObject* kwds );
      virtual Bool_t    ConvertAndSetArgs( PyObject* args, TCallContext* ctxt = 0 );
      virtual PyObject* Execute( void* self, ptrdiff_t offset, TCallContext* ctxt = 0 );

   protected:
      Cppyy::TCppMethod_t GetMethod()   { return fMethod; }
      Cppyy::TCppScope_t  GetScope()    { return fScope; }
      TExecutor*          GetExecutor() { return fExecutor; }
      std::string         GetSignatureString( Bool_t show_formalargs = kTRUE );
      std::string         GetReturnTypeName();

      virtual Bool_t InitExecutor_( TExecutor*&, TCallContext* ctxt = 0 );

   private:
      void Copy_( const TMethodHolder& );
      void Destroy_() const;

      PyObject* CallFast( void*, ptrdiff_t, TCallContext* );
      PyObject* CallSafe( void*, ptrdiff_t, TCallContext* );

      Bool_t InitConverters_();

      void SetPyError_( PyObject* msg );

   private:
   // representation
      Cppyy::TCppMethod_t fMethod;
      Cppyy::TCppScope_t  fScope;
      TExecutor*          fExecutor;

   // call dispatch buffers
      std::vector< TConverter* > fConverters;

   // cached values
      Int_t  fArgsRequired;

   // admin
      Bool_t fIsInitialized;
   };

} // namespace CPyCppyy

#endif // !CPYCPPYY_METHODHOLDER_H
