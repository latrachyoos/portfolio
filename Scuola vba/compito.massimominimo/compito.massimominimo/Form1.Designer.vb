<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form esegue l'override del metodo Dispose per pulire l'elenco dei componenti.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Richiesto da Progettazione Windows Form
    Private components As System.ComponentModel.IContainer

    'NOTA: la procedura che segue è richiesta da Progettazione Windows Form
    'Può essere modificata in Progettazione Windows Form.  
    'Non modificarla nell'editor del codice.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.dgvdati = New System.Windows.Forms.DataGridView()
        Me.btnmax = New System.Windows.Forms.Button()
        Me.btnmin = New System.Windows.Forms.Button()
        Me.btnord = New System.Windows.Forms.Button()
        CType(Me.dgvdati, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'dgvdati
        '
        Me.dgvdati.AllowUserToAddRows = False
        Me.dgvdati.AllowUserToDeleteRows = False
        Me.dgvdati.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgvdati.Location = New System.Drawing.Point(12, 12)
        Me.dgvdati.Name = "dgvdati"
        Me.dgvdati.ReadOnly = True
        Me.dgvdati.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect
        Me.dgvdati.Size = New System.Drawing.Size(607, 367)
        Me.dgvdati.TabIndex = 1
        '
        'btnmax
        '
        Me.btnmax.Location = New System.Drawing.Point(18, 391)
        Me.btnmax.Name = "btnmax"
        Me.btnmax.Size = New System.Drawing.Size(103, 61)
        Me.btnmax.TabIndex = 2
        Me.btnmax.Text = "massimo"
        Me.btnmax.UseVisualStyleBackColor = True
        '
        'btnmin
        '
        Me.btnmin.Location = New System.Drawing.Point(165, 391)
        Me.btnmin.Name = "btnmin"
        Me.btnmin.Size = New System.Drawing.Size(103, 61)
        Me.btnmin.TabIndex = 3
        Me.btnmin.Text = "minimo"
        Me.btnmin.UseVisualStyleBackColor = True
        '
        'btnord
        '
        Me.btnord.Location = New System.Drawing.Point(319, 391)
        Me.btnord.Name = "btnord"
        Me.btnord.Size = New System.Drawing.Size(103, 61)
        Me.btnord.TabIndex = 4
        Me.btnord.Text = "ordine"
        Me.btnord.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(659, 504)
        Me.Controls.Add(Me.btnord)
        Me.Controls.Add(Me.btnmin)
        Me.Controls.Add(Me.btnmax)
        Me.Controls.Add(Me.dgvdati)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgvdati, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub
    Friend WithEvents dgvdati As System.Windows.Forms.DataGridView
    Friend WithEvents btnmax As System.Windows.Forms.Button
    Friend WithEvents btnmin As System.Windows.Forms.Button
    Friend WithEvents btnord As System.Windows.Forms.Button

End Class
